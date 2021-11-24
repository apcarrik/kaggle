def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.9849, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5903, "metric_value": 0.9509, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Passanger", "instances": 5355, "metric_value": 0.936, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 3134, "metric_value": 0.9633, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Occupation", "instances": 2530, "metric_value": 0.9542, "depth": 5}
					if obj[3]>0:
						# {"feature": "Direction_same", "instances": 2494, "metric_value": 0.9561, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Education", "instances": 1499, "metric_value": 0.9679, "depth": 7}
							if obj[2]>1:
								# {"feature": "Bar", "instances": 853, "metric_value": 0.9767, "depth": 8}
								if obj[4]<=3.0:
									return 'True'
								elif obj[4]>3.0:
									return 'False'
								else: return 'False'
							elif obj[2]<=1:
								# {"feature": "Bar", "instances": 646, "metric_value": 0.9541, "depth": 8}
								if obj[4]>-1.0:
									return 'True'
								elif obj[4]<=-1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Bar", "instances": 995, "metric_value": 0.9347, "depth": 7}
							if obj[4]>-1.0:
								# {"feature": "Education", "instances": 988, "metric_value": 0.9324, "depth": 8}
								if obj[2]<=4:
									return 'True'
								elif obj[2]>4:
									return 'True'
								else: return 'True'
							elif obj[4]<=-1.0:
								# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[2]>1:
									return 'False'
								elif obj[2]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Direction_same", "instances": 36, "metric_value": 0.7107, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Bar", "instances": 24, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]<=0.0:
					# {"feature": "Occupation", "instances": 604, "metric_value": 0.9903, "depth": 5}
					if obj[3]<=21:
						# {"feature": "Education", "instances": 591, "metric_value": 0.9923, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Bar", "instances": 515, "metric_value": 0.9963, "depth": 7}
							if obj[4]>-1.0:
								# {"feature": "Direction_same", "instances": 508, "metric_value": 0.9971, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=-1.0:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Direction_same", "instances": 76, "metric_value": 0.9268, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 39, "metric_value": 0.8213, "depth": 8}
								if obj[4]<=1.0:
									return 'True'
								elif obj[4]>1.0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								# {"feature": "Bar", "instances": 37, "metric_value": 0.9868, "depth": 8}
								if obj[4]<=1.0:
									return 'True'
								elif obj[4]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[3]>21:
						# {"feature": "Direction_same", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[4]<=2.0:
									return 'True'
								else: return 'True'
							elif obj[2]>0:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 2221, "metric_value": 0.8839, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Education", "instances": 1469, "metric_value": 0.9028, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Bar", "instances": 1373, "metric_value": 0.9111, "depth": 6}
						if obj[4]<=2.0:
							# {"feature": "Occupation", "instances": 1258, "metric_value": 0.9212, "depth": 7}
							if obj[3]>1.7178390098985652:
								# {"feature": "Direction_same", "instances": 1055, "metric_value": 0.9347, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=1.7178390098985652:
								# {"feature": "Direction_same", "instances": 203, "metric_value": 0.8284, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>2.0:
							# {"feature": "Occupation", "instances": 115, "metric_value": 0.7554, "depth": 7}
							if obj[3]<=12:
								# {"feature": "Direction_same", "instances": 94, "metric_value": 0.6819, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]>12:
								# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9587, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Occupation", "instances": 96, "metric_value": 0.7383, "depth": 6}
						if obj[3]<=7:
							# {"feature": "Bar", "instances": 66, "metric_value": 0.8231, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Direction_same", "instances": 34, "metric_value": 0.7335, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								# {"feature": "Direction_same", "instances": 32, "metric_value": 0.896, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>7:
							# {"feature": "Bar", "instances": 30, "metric_value": 0.469, "depth": 7}
							if obj[4]<=1.0:
								# {"feature": "Direction_same", "instances": 29, "metric_value": 0.3621, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					# {"feature": "Bar", "instances": 752, "metric_value": 0.8414, "depth": 5}
					if obj[4]<=3.0:
						# {"feature": "Occupation", "instances": 701, "metric_value": 0.8262, "depth": 6}
						if obj[3]>2.696596706875437:
							# {"feature": "Education", "instances": 575, "metric_value": 0.8482, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 408, "metric_value": 0.8801, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 167, "metric_value": 0.752, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=2.696596706875437:
							# {"feature": "Education", "instances": 126, "metric_value": 0.7025, "depth": 7}
							if obj[2]<=4:
								# {"feature": "Direction_same", "instances": 125, "metric_value": 0.6887, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>4:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>3.0:
						# {"feature": "Occupation", "instances": 51, "metric_value": 0.9774, "depth": 6}
						if obj[3]<=12:
							# {"feature": "Education", "instances": 34, "metric_value": 0.874, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 27, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>12:
							# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]>2:
			# {"feature": "Passanger", "instances": 548, "metric_value": 0.9935, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 534, "metric_value": 0.9903, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 531, "metric_value": 0.9892, "depth": 5}
					if obj[5]>-1.0:
						# {"feature": "Bar", "instances": 528, "metric_value": 0.99, "depth": 6}
						if obj[4]>-1.0:
							# {"feature": "Occupation", "instances": 526, "metric_value": 0.9906, "depth": 7}
							if obj[3]<=7.638783269961977:
								# {"feature": "Direction_same", "instances": 335, "metric_value": 0.996, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]>7.638783269961977:
								# {"feature": "Direction_same", "instances": 191, "metric_value": 0.9756, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[5]<=1.0:
					return 'True'
				elif obj[5]>1.0:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1.0:
						return 'True'
					elif obj[4]<=1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Bar", "instances": 2244, "metric_value": 0.982, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Passanger", "instances": 1582, "metric_value": 0.9261, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 1363, "metric_value": 0.9035, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 875, "metric_value": 0.8523, "depth": 5}
					if obj[3]>2.043624253414553:
						# {"feature": "Restaurant20to50", "instances": 688, "metric_value": 0.8733, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Direction_same", "instances": 491, "metric_value": 0.8368, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 385, "metric_value": 0.8061, "depth": 8}
								if obj[7]>1:
									return 'False'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Distance", "instances": 106, "metric_value": 0.9245, "depth": 8}
								if obj[7]<=1:
									return 'False'
								elif obj[7]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]>1.0:
							# {"feature": "Distance", "instances": 197, "metric_value": 0.943, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 129, "metric_value": 0.902, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 68, "metric_value": 0.99, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=2.043624253414553:
						# {"feature": "Restaurant20to50", "instances": 187, "metric_value": 0.7588, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Direction_same", "instances": 141, "metric_value": 0.7969, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 104, "metric_value": 0.7258, "depth": 8}
								if obj[7]<=2:
									return 'False'
								elif obj[7]>2:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Distance", "instances": 37, "metric_value": 0.9353, "depth": 8}
								if obj[7]<=1:
									return 'False'
								elif obj[7]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=0.0:
							# {"feature": "Direction_same", "instances": 46, "metric_value": 0.6153, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 35, "metric_value": 0.7219, "depth": 8}
								if obj[7]>1:
									return 'False'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 488, "metric_value": 0.967, "depth": 5}
					if obj[3]>1.348010951701891:
						# {"feature": "Restaurant20to50", "instances": 406, "metric_value": 0.9872, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Distance", "instances": 379, "metric_value": 0.9824, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 228, "metric_value": 0.9754, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 151, "metric_value": 0.9908, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							# {"feature": "Distance", "instances": 27, "metric_value": 0.9751, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=1.348010951701891:
						# {"feature": "Restaurant20to50", "instances": 82, "metric_value": 0.7121, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Distance", "instances": 56, "metric_value": 0.8631, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Direction_same", "instances": 43, "metric_value": 0.9103, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]>2:
								# {"feature": "Direction_same", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Restaurant20to50", "instances": 219, "metric_value": 0.9988, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Education", "instances": 160, "metric_value": 0.9863, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Occupation", "instances": 126, "metric_value": 0.9587, "depth": 6}
						if obj[3]>0:
							# {"feature": "Distance", "instances": 123, "metric_value": 0.9474, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 102, "metric_value": 0.9278, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9984, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 6}
						if obj[3]<=12:
							# {"feature": "Distance", "instances": 31, "metric_value": 0.9812, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 26, "metric_value": 0.9612, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>12:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					# {"feature": "Education", "instances": 59, "metric_value": 0.9647, "depth": 5}
					if obj[2]>0:
						# {"feature": "Occupation", "instances": 44, "metric_value": 0.9985, "depth": 6}
						if obj[3]<=12:
							# {"feature": "Distance", "instances": 42, "metric_value": 1.0, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 40, "metric_value": 0.9982, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						elif obj[3]>12:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 6}
						if obj[3]>3:
							# {"feature": "Distance", "instances": 14, "metric_value": 0.3712, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						elif obj[3]<=3:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Restaurant20to50", "instances": 662, "metric_value": 0.9636, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Passanger", "instances": 355, "metric_value": 0.9975, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 290, "metric_value": 1.0, "depth": 5}
					if obj[3]<=13.855047474895077:
						# {"feature": "Direction_same", "instances": 241, "metric_value": 0.9972, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Distance", "instances": 183, "metric_value": 0.9998, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Education", "instances": 135, "metric_value": 0.9933, "depth": 8}
								if obj[2]<=3:
									return 'False'
								elif obj[2]>3:
									return 'True'
								else: return 'True'
							elif obj[7]>2:
								# {"feature": "Education", "instances": 48, "metric_value": 0.9685, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Education", "instances": 58, "metric_value": 0.9294, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Distance", "instances": 52, "metric_value": 0.9118, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>13.855047474895077:
						# {"feature": "Distance", "instances": 49, "metric_value": 0.9313, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Direction_same", "instances": 38, "metric_value": 0.868, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Education", "instances": 27, "metric_value": 0.7642, "depth": 8}
								if obj[2]<=3:
									return 'False'
								elif obj[2]>3:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[2]<=2:
									return 'True'
								elif obj[2]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[7]>2:
							# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Occupation", "instances": 65, "metric_value": 0.9233, "depth": 5}
					if obj[3]<=10:
						# {"feature": "Education", "instances": 48, "metric_value": 0.9685, "depth": 6}
						if obj[2]>0:
							# {"feature": "Distance", "instances": 26, "metric_value": 0.9957, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 19, "metric_value": 0.998, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 19, "metric_value": 0.9495, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>10:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.6723, "depth": 6}
						if obj[7]>1:
							# {"feature": "Education", "instances": 16, "metric_value": 0.5436, "depth": 7}
							if obj[2]>1:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[5]>1.0:
				# {"feature": "Direction_same", "instances": 307, "metric_value": 0.8728, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Education", "instances": 250, "metric_value": 0.917, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 161, "metric_value": 0.9656, "depth": 6}
						if obj[3]>1:
							# {"feature": "Distance", "instances": 133, "metric_value": 0.9882, "depth": 7}
							if obj[7]>1:
								# {"feature": "Passanger", "instances": 94, "metric_value": 0.979, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Passanger", "instances": 39, "metric_value": 0.9995, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=1:
							# {"feature": "Distance", "instances": 28, "metric_value": 0.6769, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.8113, "depth": 8}
								if obj[0]>0:
									return 'True'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]>2:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 89, "metric_value": 0.7687, "depth": 6}
						if obj[3]<=10:
							# {"feature": "Passanger", "instances": 53, "metric_value": 0.9052, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Distance", "instances": 42, "metric_value": 0.8631, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[7]>1:
									return 'True'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>10:
							# {"feature": "Passanger", "instances": 36, "metric_value": 0.4138, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[7]>1:
									return 'True'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>0:
					# {"feature": "Occupation", "instances": 57, "metric_value": 0.5374, "depth": 5}
					if obj[3]<=22:
						# {"feature": "Passanger", "instances": 54, "metric_value": 0.5564, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 52, "metric_value": 0.57, "depth": 7}
							if obj[2]<=4:
								# {"feature": "Distance", "instances": 50, "metric_value": 0.5842, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							elif obj[2]>4:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[3]>22:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
