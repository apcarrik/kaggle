def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 89, "metric_value": 0.9513, "depth": 2}
		if obj[0]>0:
			# {"feature": "Time", "instances": 82, "metric_value": 0.9724, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 67, "metric_value": 0.996, "depth": 4}
				if obj[8]<=2:
					# {"feature": "Direction_same", "instances": 58, "metric_value": 0.9784, "depth": 5}
					if obj[7]<=0:
						# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.9968, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Bar", "instances": 36, "metric_value": 0.9799, "depth": 7}
							if obj[5]<=3.0:
								# {"feature": "Occupation", "instances": 35, "metric_value": 0.971, "depth": 8}
								if obj[4]<=17:
									# {"feature": "Education", "instances": 30, "metric_value": 0.9871, "depth": 9}
									if obj[3]<=3:
										return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								elif obj[4]>17:
									# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[3]>1:
										return 'True'
									elif obj[3]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>3.0:
								return 'False'
							else: return 'False'
						elif obj[6]<=0.0:
							# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=6:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=0.0:
										return 'True'
									elif obj[5]>0.0:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>6:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[7]>0:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[4]>2:
							# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=2.0:
										return 'False'
									elif obj[5]>2.0:
										return 'True'
									else: return 'True'
								elif obj[6]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[3]>2:
								# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>0.0:
										return 'False'
									elif obj[6]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[5]>0.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[8]>2:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[6]<=1.0:
						return 'False'
					elif obj[6]>1.0:
						# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>4:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=2.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=4:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[6]>0.0:
					return 'True'
				elif obj[6]<=0.0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]<=4:
						return 'False'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 38, "metric_value": 0.9268, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Bar", "instances": 27, "metric_value": 0.8256, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.684, "depth": 4}
				if obj[6]>-1.0:
					# {"feature": "Education", "instances": 21, "metric_value": 0.5917, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 6}
						if obj[4]<=10:
							return 'False'
						elif obj[4]>10:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[5]>2.0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[4]<=13:
				# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=1.0:
							return 'False'
						elif obj[6]>1.0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>13:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
