def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9762, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Age", "instances": 98, "metric_value": 0.9973, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Distance", "instances": 93, "metric_value": 0.9899, "depth": 3}
			if obj[12]>1:
				# {"feature": "Coffeehouse", "instances": 49, "metric_value": 0.9925, "depth": 4}
				if obj[9]<=2.0:
					# {"feature": "Occupation", "instances": 37, "metric_value": 0.9569, "depth": 5}
					if obj[7]<=16:
						# {"feature": "Time", "instances": 34, "metric_value": 0.9774, "depth": 6}
						if obj[1]>0:
							# {"feature": "Children", "instances": 27, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								# {"feature": "Coupon", "instances": 14, "metric_value": 0.5917, "depth": 8}
								if obj[2]<=2:
									return 'False'
								elif obj[2]>2:
									# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[6]>3:
											return 'False'
										else: return 'False'
									elif obj[10]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]<=0:
								# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[2]>0:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[3]>0:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[10]<=0.0:
														return 'True'
													elif obj[10]>0.0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[10]>0.0:
														return 'False'
													elif obj[10]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										elif obj[2]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										return 'False'
									else: return 'False'
								elif obj[6]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>16:
						return 'False'
					else: return 'False'
				elif obj[9]>2.0:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[7]>1:
							return 'True'
						elif obj[7]<=1:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]>1.0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>1:
							# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]<=1:
				# {"feature": "Education", "instances": 44, "metric_value": 0.9024, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Gender", "instances": 34, "metric_value": 0.7871, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[7]>4:
							# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>0.0:
										return 'True'
									elif obj[8]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[10]<=2.0:
										return 'False'
									elif obj[10]>2.0:
										return 'True'
									else: return 'True'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]<=4:
							return 'False'
						else: return 'False'
					elif obj[3]>0:
						# {"feature": "Children", "instances": 17, "metric_value": 0.5226, "depth": 6}
						if obj[5]>0:
							# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[7]<=11:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[10]<=3.0:
									return 'True'
								elif obj[10]>3.0:
									return 'False'
								else: return 'False'
							elif obj[7]>11:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>2:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[2]>1:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]>3:
								return 'False'
							elif obj[7]<=3:
								return 'True'
							else: return 'True'
						elif obj[10]>2.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>6:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.7355, "depth": 2}
		if obj[9]>1.0:
			# {"feature": "Time", "instances": 17, "metric_value": 0.3228, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>2:
					return 'True'
				elif obj[4]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]<=1.0:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[2]>0:
				# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[7]<=7:
						# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[4]<=5:
							return 'True'
						elif obj[4]>5:
							# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[7]>7:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
