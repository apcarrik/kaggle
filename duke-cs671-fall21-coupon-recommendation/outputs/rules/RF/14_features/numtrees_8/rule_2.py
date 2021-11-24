def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 87, "metric_value": 0.9396, "depth": 2}
		if obj[7]>1:
			# {"feature": "Age", "instances": 78, "metric_value": 0.9694, "depth": 3}
			if obj[4]>2:
				# {"feature": "Distance", "instances": 42, "metric_value": 0.9984, "depth": 4}
				if obj[13]<=2:
					# {"feature": "Education", "instances": 38, "metric_value": 0.998, "depth": 5}
					if obj[6]<=3:
						# {"feature": "Direction_same", "instances": 35, "metric_value": 0.9994, "depth": 6}
						if obj[12]<=0:
							# {"feature": "Income", "instances": 29, "metric_value": 0.9923, "depth": 7}
							if obj[8]>4:
								# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=1.0:
									# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[1]>0:
										# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[5]>0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[5]<=0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[0]>0:
												return 'True'
											elif obj[0]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[11]>1.0:
									return 'True'
								else: return 'True'
							elif obj[8]<=4:
								# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[11]<=1.0:
									# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[10]<=3.0:
											# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[1]>0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[0]>0:
													# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[3]<=0:
														# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[5]<=0:
															return 'True'
														elif obj[5]>0:
															return 'False'
														else: return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[0]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]>3.0:
											return 'False'
										else: return 'False'
									elif obj[9]>2.0:
										return 'False'
									else: return 'False'
								elif obj[11]>1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[12]>0:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[10]<=3.0:
								return 'False'
							elif obj[10]>3.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>3:
						return 'True'
					else: return 'True'
				elif obj[13]>2:
					return 'False'
				else: return 'False'
			elif obj[4]<=2:
				# {"feature": "Income", "instances": 36, "metric_value": 0.8113, "depth": 4}
				if obj[8]>2:
					# {"feature": "Education", "instances": 25, "metric_value": 0.6343, "depth": 5}
					if obj[6]>1:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[10]>1.0:
									return 'True'
								elif obj[10]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[9]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[6]<=1:
						return 'True'
					else: return 'True'
				elif obj[8]<=2:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[13]>1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]>0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[13]<=1:
							return 'True'
						else: return 'True'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Income", "instances": 40, "metric_value": 0.9837, "depth": 2}
		if obj[8]<=4:
			# {"feature": "Gender", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[13]<=2:
					return 'True'
				elif obj[13]>2:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10]>0.0:
						return 'False'
					elif obj[10]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>0:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>3:
						return 'False'
					elif obj[1]<=3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>4:
			# {"feature": "Children", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[10]<=2.0:
						return 'False'
					elif obj[10]>2.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	else: return 'False'
