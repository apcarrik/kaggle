def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 95, "metric_value": 0.9903, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Bar", "instances": 68, "metric_value": 0.9975, "depth": 3}
			if obj[8]<=3.0:
				# {"feature": "Restaurant20to50", "instances": 65, "metric_value": 0.9916, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Education", "instances": 44, "metric_value": 0.9985, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Time", "instances": 37, "metric_value": 0.9953, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 27, "metric_value": 0.9751, "depth": 7}
							if obj[7]<=13:
								# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.9024, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Gender", "instances": 14, "metric_value": 0.7496, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[9]>1.0:
									# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[12]>1:
										# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]>0:
													return 'False'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									elif obj[12]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>13:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[4]<=3:
									return 'True'
								elif obj[4]>3:
									# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9]>0.0:
										return 'True'
									elif obj[9]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[7]>4:
								return 'True'
							elif obj[7]<=4:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[6]>2:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[7]>1:
							return 'False'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[10]>1.0:
					# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.8631, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[4]<=1:
							# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[7]<=4:
								return 'True'
							elif obj[7]>4:
								# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>1:
							return 'False'
						else: return 'False'
					elif obj[9]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[8]>3.0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Bar", "instances": 27, "metric_value": 0.7642, "depth": 3}
			if obj[8]<=1.0:
				# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[9]<=2.0:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 5}
					if obj[7]>0:
						# {"feature": "Time", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Children", "instances": 13, "metric_value": 0.3912, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>1:
									return 'False'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]>1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				elif obj[9]>2.0:
					return 'True'
				else: return 'True'
			elif obj[8]>1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Bar", "instances": 32, "metric_value": 0.896, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[7]>1:
				# {"feature": "Age", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[2]>1:
						# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]>0:
										return 'True'
									elif obj[6]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[9]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			elif obj[7]<=1:
				return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
