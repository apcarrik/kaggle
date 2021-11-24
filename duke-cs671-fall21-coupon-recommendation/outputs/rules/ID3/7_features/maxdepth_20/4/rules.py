def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.9876, "depth": 1}
	if obj[1]>1:
		# {"feature": "Passanger", "instances": 5867, "metric_value": 0.9568, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Distance", "instances": 3640, "metric_value": 0.982, "depth": 3}
			if obj[6]<=1:
				# {"feature": "Restaurant20to50", "instances": 1967, "metric_value": 0.9259, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Direction_same", "instances": 1583, "metric_value": 0.9134, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Education", "instances": 863, "metric_value": 0.8898, "depth": 6}
						if obj[2]<=4:
							# {"feature": "Occupation", "instances": 854, "metric_value": 0.8935, "depth": 7}
							if obj[3]<=7.901639344262295:
								return 'True'
							elif obj[3]>7.901639344262295:
								return 'True'
							else: return 'True'
						elif obj[2]>4:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						# {"feature": "Occupation", "instances": 720, "metric_value": 0.9377, "depth": 6}
						if obj[3]>0:
							# {"feature": "Education", "instances": 716, "metric_value": 0.9394, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Occupation", "instances": 384, "metric_value": 0.9669, "depth": 5}
					if obj[3]<=13:
						# {"feature": "Education", "instances": 354, "metric_value": 0.959, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Direction_same", "instances": 281, "metric_value": 0.9742, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 73, "metric_value": 0.8657, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>13:
						# {"feature": "Education", "instances": 30, "metric_value": 0.9968, "depth": 6}
						if obj[2]>2:
							# {"feature": "Direction_same", "instances": 18, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=2:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[6]>1:
				# {"feature": "Direction_same", "instances": 1673, "metric_value": 0.9993, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Education", "instances": 1336, "metric_value": 0.9955, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 886, "metric_value": 0.988, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Occupation", "instances": 549, "metric_value": 0.9942, "depth": 7}
							if obj[3]<=13.745627663558507:
								return 'False'
							elif obj[3]>13.745627663558507:
								return 'True'
							else: return 'True'
						elif obj[4]>1.0:
							# {"feature": "Occupation", "instances": 337, "metric_value": 0.973, "depth": 7}
							if obj[3]<=18.494252182222326:
								return 'False'
							elif obj[3]>18.494252182222326:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 450, "metric_value": 0.9998, "depth": 6}
						if obj[4]<=2.0:
							# {"feature": "Occupation", "instances": 426, "metric_value": 0.9999, "depth": 7}
							if obj[3]>1.7153603235224644:
								return 'True'
							elif obj[3]<=1.7153603235224644:
								return 'False'
							else: return 'False'
						elif obj[4]>2.0:
							# {"feature": "Occupation", "instances": 24, "metric_value": 0.8113, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>0:
					# {"feature": "Restaurant20to50", "instances": 337, "metric_value": 0.9807, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Occupation", "instances": 241, "metric_value": 0.9955, "depth": 6}
						if obj[3]>0:
							# {"feature": "Education", "instances": 238, "metric_value": 0.9967, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Occupation", "instances": 96, "metric_value": 0.896, "depth": 6}
						if obj[3]>3:
							# {"feature": "Education", "instances": 69, "metric_value": 0.8281, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[3]<=3:
							# {"feature": "Education", "instances": 27, "metric_value": 0.9911, "depth": 7}
							if obj[2]<=3:
								return 'True'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Education", "instances": 2227, "metric_value": 0.8909, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 1463, "metric_value": 0.9057, "depth": 4}
				if obj[3]<=19.11385554190759:
					# {"feature": "Restaurant20to50", "instances": 1386, "metric_value": 0.8992, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Distance", "instances": 1265, "metric_value": 0.893, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 832, "metric_value": 0.8833, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 433, "metric_value": 0.9104, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						# {"feature": "Distance", "instances": 121, "metric_value": 0.9521, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 73, "metric_value": 0.8989, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 48, "metric_value": 0.995, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>19.11385554190759:
					# {"feature": "Restaurant20to50", "instances": 77, "metric_value": 0.9852, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 56, "metric_value": 0.9241, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 43, "metric_value": 0.933, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Distance", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 764, "metric_value": 0.8591, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 562, "metric_value": 0.8886, "depth": 5}
					if obj[3]<=18.63348904995262:
						# {"feature": "Distance", "instances": 520, "metric_value": 0.9014, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 346, "metric_value": 0.8712, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 174, "metric_value": 0.949, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>18.63348904995262:
						# {"feature": "Distance", "instances": 42, "metric_value": 0.65, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 25, "metric_value": 0.6343, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 17, "metric_value": 0.6723, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 202, "metric_value": 0.7562, "depth": 5}
					if obj[3]<=18:
						# {"feature": "Distance", "instances": 196, "metric_value": 0.7683, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 131, "metric_value": 0.8021, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 65, "metric_value": 0.6901, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 2281, "metric_value": 0.9817, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Occupation", "instances": 1500, "metric_value": 0.9481, "depth": 3}
			if obj[3]>1.9904707123952177:
				# {"feature": "Passanger", "instances": 1255, "metric_value": 0.9646, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 1087, "metric_value": 0.9533, "depth": 5}
					if obj[2]>0:
						# {"feature": "Direction_same", "instances": 730, "metric_value": 0.9284, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 569, "metric_value": 0.9117, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 161, "metric_value": 0.9731, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 357, "metric_value": 0.9875, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 281, "metric_value": 0.9797, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							# {"feature": "Direction_same", "instances": 76, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 168, "metric_value": 0.9999, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 140, "metric_value": 0.9987, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 113, "metric_value": 0.9995, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 27, "metric_value": 0.9911, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 28, "metric_value": 0.9852, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9656, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=1.9904707123952177:
				# {"feature": "Education", "instances": 245, "metric_value": 0.8097, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Direction_same", "instances": 225, "metric_value": 0.7722, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 173, "metric_value": 0.7149, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 137, "metric_value": 0.6357, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Distance", "instances": 36, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>0:
						# {"feature": "Distance", "instances": 52, "metric_value": 0.9118, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Passanger", "instances": 38, "metric_value": 0.9268, "depth": 7}
							if obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 20, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[6]<=2:
								return 'True'
							elif obj[6]>2:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Distance", "instances": 781, "metric_value": 0.9984, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Education", "instances": 641, "metric_value": 0.9939, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 442, "metric_value": 0.9993, "depth": 5}
					if obj[3]<=19.17084245775628:
						# {"feature": "Passanger", "instances": 415, "metric_value": 0.9985, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 365, "metric_value": 0.9996, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							# {"feature": "Direction_same", "instances": 50, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>19.17084245775628:
						# {"feature": "Passanger", "instances": 27, "metric_value": 0.9751, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9341, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 199, "metric_value": 0.9628, "depth": 5}
					if obj[3]<=9:
						# {"feature": "Passanger", "instances": 132, "metric_value": 0.9919, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 110, "metric_value": 0.9979, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Direction_same", "instances": 22, "metric_value": 0.9024, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>9:
						# {"feature": "Passanger", "instances": 67, "metric_value": 0.8395, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 60, "metric_value": 0.8813, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]>2:
				# {"feature": "Passanger", "instances": 140, "metric_value": 0.9821, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 139, "metric_value": 0.9802, "depth": 5}
					if obj[3]>0:
						# {"feature": "Education", "instances": 138, "metric_value": 0.9781, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Direction_same", "instances": 102, "metric_value": 0.9864, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 36, "metric_value": 0.9436, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
