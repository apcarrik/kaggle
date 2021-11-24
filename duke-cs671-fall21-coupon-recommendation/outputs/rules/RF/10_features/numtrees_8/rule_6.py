def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[4]>1.6321624278212852:
		# {"feature": "Coffeehouse", "instances": 104, "metric_value": 0.9904, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Passanger", "instances": 81, "metric_value": 0.9999, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 60, "metric_value": 0.9871, "depth": 4}
				if obj[3]>1:
					# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.909, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Bar", "instances": 34, "metric_value": 0.9367, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Coupon", "instances": 33, "metric_value": 0.9457, "depth": 7}
							if obj[2]>1:
								# {"feature": "Distance", "instances": 21, "metric_value": 0.9852, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Time", "instances": 19, "metric_value": 0.9495, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>2:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[9]<=1:
									# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[7]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=1:
					# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9]>1:
										return 'False'
									elif obj[9]<=1:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=0.0:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[8]<=0:
								return 'False'
							elif obj[8]>0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[7]>1.0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[9]<=2:
							return 'True'
						elif obj[9]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Distance", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[9]>1:
					# {"feature": "Time", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[2]>2:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]>0.0:
										return 'False'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=2:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[9]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]<=0.0:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.7554, "depth": 3}
			if obj[2]>2:
				# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[5]<=0.0:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[1]>0:
								# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[0]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[0]<=1:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9]<=2:
										return 'False'
									elif obj[9]>2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]>1.0:
							return 'False'
						else: return 'False'
					elif obj[5]>0.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]<=1.6321624278212852:
		# {"feature": "Time", "instances": 23, "metric_value": 0.8281, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[3]>0:
							# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[9]>2:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=2:
									return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[6]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	else: return 'True'
