def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 86, "metric_value": 0.9606, "depth": 2}
		if obj[6]<=10:
			# {"feature": "Education", "instances": 65, "metric_value": 0.8905, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Age", "instances": 49, "metric_value": 0.8031, "depth": 4}
				if obj[4]>0:
					# {"feature": "Bar", "instances": 43, "metric_value": 0.8542, "depth": 5}
					if obj[7]<=2.0:
						# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.8296, "depth": 6}
						if obj[9]<=2.0:
							# {"feature": "Distance", "instances": 40, "metric_value": 0.8485, "depth": 7}
							if obj[11]>1:
								# {"feature": "Time", "instances": 21, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									# {"feature": "Passanger", "instances": 18, "metric_value": 0.9641, "depth": 9}
									if obj[0]>0:
										# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9367, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[11]<=1:
								# {"feature": "Time", "instances": 19, "metric_value": 0.7425, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 14, "metric_value": 0.8631, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[0]<=1:
													return 'True'
												elif obj[0]>1:
													return 'True'
												else: return 'True'
											elif obj[8]>1.0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[0]<=1:
													return 'False'
												elif obj[0]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[10]>0:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[9]>2.0:
							return 'True'
						else: return 'True'
					elif obj[7]>2.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]>2:
				# {"feature": "Distance", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[11]<=1:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[8]>1.0:
						return 'True'
					elif obj[8]<=1.0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>1:
							return 'False'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>1:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]<=0:
						return 'False'
					elif obj[3]>0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[6]>10:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[5]>0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]>1.0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=4:
										return 'False'
									elif obj[4]>4:
										return 'True'
									else: return 'True'
								elif obj[8]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=0:
							return 'False'
						elif obj[4]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[9]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 41, "metric_value": 0.9262, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Occupation", "instances": 26, "metric_value": 0.7793, "depth": 3}
			if obj[6]<=14:
				# {"feature": "Bar", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Age", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.5665, "depth": 6}
						if obj[9]<=2.0:
							# {"feature": "Distance", "instances": 14, "metric_value": 0.3712, "depth": 7}
							if obj[11]<=1:
								return 'False'
							elif obj[11]>1:
								# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[9]>2.0:
							return 'True'
						else: return 'True'
					elif obj[4]>4:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>2.0:
					return 'True'
				else: return 'True'
			elif obj[6]>14:
				return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6]<=5:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=4:
								return 'False'
							elif obj[4]>4:
								return 'True'
							else: return 'True'
						elif obj[6]>5:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[7]>2.0:
					return 'False'
				else: return 'False'
			elif obj[5]>2:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=7:
					return 'False'
				elif obj[6]>7:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
