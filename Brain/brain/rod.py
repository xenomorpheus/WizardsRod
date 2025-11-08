"""Rod"""

import logging

from typing import List, Dict
from brain.spell import Spell
from brain.spelllistprepared import SpellListPrepared
from brain.hardware import Hardware
from brain.hardwarefetch import HardwareFetch
from brain.rodevent import RodEvent


class Rod:
    """The Rod brings together the prepared spells and the hardware.

    The Rod listens for events from the hardware, and passes them to the prepared spell list.
    The prepared spell list reports which spells have the trigger sequence completed.
    Those spells have their actions performed by the Rod.

    The Rod needs to pass on events to the prepared spell list, rather than have the prepared spell list
    listen to hardware directly, because the rod needs to know which spells have been activated, in order
    to perform their actions.

    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.logger = logging.getLogger(__name__)
        self.spell_list_prepared = SpellListPrepared()
        """ a list of spells we are waiting for events in order to activate """
        self.hwf = HardwareFetch()
        """ object for fetching hardware interfaces """
        self.hardware = {}  # type: Dict[str, Hardware]
        """ hardware interface objects. keyed by hardware hint string """

    def get_name(self) -> str:
        """get the name"""
        return self.name

    def spell_add(self, spell: Spell) -> "Rod":
        """add a spell to the prepared list"""
        self.spell_list_prepared.spell_add(spell)
        self.__recalculate_hardware()
        return self

    def spell_add_list(self, spelllist) -> "Rod":
        """add a list of spells to the prepared list"""
        self.spell_list_prepared.spell_add_list(spelllist)
        self.__recalculate_hardware()
        return self

    def spell_del(self, spell: Spell) -> "Rod":
        """remove a spell from the prepared list"""
        self.spell_list_prepared.spell_del(spell)
        self.__recalculate_hardware()
        return self

    def receive_events(self, new_events: List[RodEvent]) -> None:
        """receive events"""
        for event in new_events:
            self.receive_event(event)

    def receive_event(self, event: RodEvent) -> None:
        """receive an event"""
        for spell in self.spell_list_prepared.receive_event(event):
            self.logger.info(
                "Activating spell='%s' for rod='%s'",
                spell.get_name(),
                self.get_name(),
            )
            callable = spell.get_perform_action()
            if callable is not None:
                callable(spell, self)

    def testing_get_hwf(self) -> HardwareFetch:
        """get the hardware fetch object. Only used in testing."""
        return self.hwf

    def __deactivate_hardware(self, hardware_hint: str) -> None:
        self.logger.debug("Deactivating hardware: %s", hardware_hint)
        hardware = self.hardware[hardware_hint]
        hardware.listener_remove(self)
        hardware.deactivate()
        del self.hardware[hardware_hint]

    def __recalculate_hardware(self) -> None:
        hardware_hints_new = self.spell_list_prepared.get_hardware_hints()

        # Deactivate and remove hardware no longer needed
        for hardware_hint in self.hardware.keys() - hardware_hints_new:
            self.__deactivate_hardware(hardware_hint)

        # Activate and add newly needed hardware
        for hardware_hint in hardware_hints_new - self.hardware.keys():
            self.logger.debug("Activating hardware: %s", hardware_hint)
            hardware = self.hwf.get(hardware_hint)
            hardware.listener_add(self)
            self.hardware[hardware_hint] = hardware
            hardware.activate()

    def end(self) -> "Rod":
        """shut down the hardware"""
        for hardware_hint in list(self.hardware):
            self.__deactivate_hardware(hardware_hint)
        return self

    def __del__(self):
        """destructor"""
        self.end()
