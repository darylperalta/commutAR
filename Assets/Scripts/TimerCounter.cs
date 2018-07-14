using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TimerCounter : MonoBehaviour {

	int start = 336;
	Text text;
	
	void Start () {
		InvokeRepeating("tick", 0f, 1f);
		text = GetComponent<Text>();
	}
	void tick() {
		text.text = (start / 60).ToString();
		text.text += ":";
		text.text += (start % 60).ToString("00");
		text.text += " mins";
		start--;
		if (start < 0)
			CancelInvoke("tick");
	}
}
