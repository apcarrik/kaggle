def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 89, "metric_value": 0.9513, "depth": 2}
		if obj[6]<=10:
			# {"feature": "Education", "instances": 72, "metric_value": 0.888, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Bar", "instances": 68, "metric_value": 0.9082, "depth": 4}
				if obj[7]<=3.0:
					# {"feature": "Gender", "instances": 67, "metric_value": 0.8971, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.7755, "depth": 6}
						if obj[9]<=3.0:
							# {"feature": "Passanger", "instances": 34, "metric_value": 0.7335, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 23, "metric_value": 0.8865, "depth": 8}
								if obj[1]>0:
									# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 11}
											if obj[4]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[4]<=0:
												return 'True'
											else: return 'True'
										elif obj[11]>2:
											return 'True'
										else: return 'True'
									elif obj[8]>3.0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4]>4:
											return 'False'
										elif obj[4]<=4:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[11]<=1:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4]<=1:
											return 'True'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									elif obj[11]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[9]>3.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						# {"feature": "Time", "instances": 32, "metric_value": 0.9745, "depth": 6}
						if obj[1]>0:
							# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.9957, "depth": 7}
							if obj[8]>0.0:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 8}
								if obj[0]>1:
									# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[4]>0:
										# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[11]>1:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9]>0.0:
													return 'False'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									elif obj[4]>4:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]<=0.0:
								# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[4]>1:
									# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[11]>1:
												return 'False'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[4]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]<=0:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[10]<=0:
								return 'True'
							elif obj[10]>0:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=4:
									return 'True'
								elif obj[4]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[7]>3.0:
					return 'False'
				else: return 'False'
			elif obj[5]>3:
				return 'True'
			else: return 'True'
		elif obj[6]>10:
			# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[8]<=2.0:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[9]>0.0:
					# {"feature": "Gender", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[3]>0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4]<=2:
									return 'False'
								elif obj[4]>2:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0.0:
										return 'False'
									elif obj[7]>0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[9]<=0.0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 38, "metric_value": 0.9495, "depth": 2}
		if obj[6]>1:
			# {"feature": "Coffeehouse", "instances": 32, "metric_value": 0.8571, "depth": 3}
			if obj[8]>1.0:
				# {"feature": "Age", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[7]<=2.0:
							# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[0]>0:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[11]<=2:
										return 'True'
									elif obj[11]>2:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>1.0:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]>2.0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				elif obj[4]>3:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=0:
							return 'True'
						elif obj[3]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=1.0:
				# {"feature": "Age", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[6]<=1:
			# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[9]>0.0:
				return 'True'
			elif obj[9]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
