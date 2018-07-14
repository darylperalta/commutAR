using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PanelCloser : MonoBehaviour {

	public GameObject panel;

	public void close() {
		panel.GetComponent<Canvas>().enabled = false;
	}


}
