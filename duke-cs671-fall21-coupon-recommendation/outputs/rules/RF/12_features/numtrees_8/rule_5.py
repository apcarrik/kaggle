def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[5]<=3:
		# {"feature": "Occupation", "instances": 115, "metric_value": 0.9995, "depth": 2}
		if obj[6]<=12.937768545455379:
			# {"feature": "Coupon", "instances": 100, "metric_value": 0.9974, "depth": 3}
			if obj[2]>1:
				# {"feature": "Passanger", "instances": 74, "metric_value": 0.974, "depth": 4}
				if obj[0]>0:
					# {"feature": "Age", "instances": 70, "metric_value": 0.9852, "depth": 5}
					if obj[4]>1:
						# {"feature": "Gender", "instances": 52, "metric_value": 0.9989, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.9403, "depth": 7}
							if obj[9]>-1.0:
								# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Distance", "instances": 25, "metric_value": 0.9427, "depth": 9}
									if obj[11]>1:
										# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 10}
										if obj[1]>0:
											# {"feature": "Bar", "instances": 14, "metric_value": 0.7496, "depth": 11}
											if obj[7]<=1.0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[7]>1.0:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[11]<=1:
										# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 10}
										if obj[7]>1.0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[10]>0:
												# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1]>0:
													return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												return 'False'
											else: return 'False'
										elif obj[7]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]>3.0:
									return 'True'
								else: return 'True'
							elif obj[9]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[3]>0:
							# {"feature": "Bar", "instances": 24, "metric_value": 0.9544, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9852, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9968, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[11]>2:
												return 'True'
											else: return 'True'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=0.0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[1]>0:
										return 'False'
									elif obj[1]<=0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=0.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>2.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=1:
						# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.8524, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Time", "instances": 16, "metric_value": 0.6962, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[11]>2:
										return 'True'
									else: return 'True'
								elif obj[9]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						elif obj[8]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Bar", "instances": 26, "metric_value": 0.9306, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[1]>0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						elif obj[8]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[9]>1.0:
						return 'False'
					else: return 'False'
				elif obj[7]>1.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[9]>1.0:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[9]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>12.937768545455379:
			# {"feature": "Age", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=5:
				# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[8]<=3.0:
					return 'False'
				elif obj[8]>3.0:
					return 'True'
				else: return 'True'
			elif obj[4]>5:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]>3:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[0]<=1:
			return 'True'
		elif obj[0]>1:
			# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[7]>0.0:
				return 'False'
			elif obj[7]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
