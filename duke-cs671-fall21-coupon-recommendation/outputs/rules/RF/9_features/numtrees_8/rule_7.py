def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Distance", "instances": 90, "metric_value": 0.9968, "depth": 2}
		if obj[8]<=1:
			# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.971, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Occupation", "instances": 38, "metric_value": 0.8997, "depth": 4}
				if obj[4]<=14:
					# {"feature": "Time", "instances": 36, "metric_value": 0.8524, "depth": 5}
					if obj[1]>0:
						# {"feature": "Bar", "instances": 26, "metric_value": 0.9306, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 7}
							if obj[3]>1:
								# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[2]>0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[2]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[2]>0:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[3]<=1:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>1:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[4]>14:
					return 'False'
				else: return 'False'
			elif obj[6]<=0.0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[4]<=6:
					return 'False'
				elif obj[4]>6:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>1:
			# {"feature": "Coupon", "instances": 45, "metric_value": 0.9183, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 40, "metric_value": 0.9544, "depth": 4}
				if obj[4]>4:
					# {"feature": "Education", "instances": 29, "metric_value": 0.8498, "depth": 5}
					if obj[3]>1:
						# {"feature": "Bar", "instances": 17, "metric_value": 0.6723, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]>1.0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[1]<=1:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[6]>2.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=1:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>2.0:
									return 'True'
								else: return 'True'
							elif obj[7]>0:
								return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]<=4:
					# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[3]>1:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[6]>1.0:
										return 'False'
									elif obj[6]<=1.0:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[5]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Bar", "instances": 37, "metric_value": 0.878, "depth": 2}
		if obj[5]<=2.0:
			# {"feature": "Occupation", "instances": 35, "metric_value": 0.8224, "depth": 3}
			if obj[4]<=7:
				# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 5}
					if obj[2]>2:
						# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]>2:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[8]>1:
								return 'True'
							elif obj[8]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]<=2:
						# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[8]>1:
									# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2.0:
					return 'False'
				else: return 'False'
			elif obj[4]>7:
				return 'True'
			else: return 'True'
		elif obj[5]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'
