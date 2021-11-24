def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[2]>1:
		# {"feature": "Age", "instances": 93, "metric_value": 0.9629, "depth": 2}
		if obj[4]>2:
			# {"feature": "Bar", "instances": 50, "metric_value": 0.8267, "depth": 3}
			if obj[8]<=2.0:
				# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.7467, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Occupation", "instances": 35, "metric_value": 0.5127, "depth": 5}
					if obj[7]<=19:
						# {"feature": "Education", "instances": 34, "metric_value": 0.4306, "depth": 6}
						if obj[6]<=0:
							return 'True'
						elif obj[6]>0:
							# {"feature": "Distance", "instances": 17, "metric_value": 0.6723, "depth": 7}
							if obj[12]<=1:
								# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[0]>1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]<=1:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									elif obj[11]>0:
										return 'True'
									else: return 'True'
								elif obj[9]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[12]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>19:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[7]<=5:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]>1:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					elif obj[7]>5:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[8]>2.0:
				return 'False'
			else: return 'False'
		elif obj[4]<=2:
			# {"feature": "Passanger", "instances": 43, "metric_value": 0.9965, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 30, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=21:
					# {"feature": "Time", "instances": 28, "metric_value": 0.8631, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.971, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 7}
							if obj[6]<=4:
								# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.8113, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 9}
									if obj[12]<=2:
										# {"feature": "Children", "instances": 12, "metric_value": 0.8113, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[8]>3.0:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									elif obj[12]>2:
										return 'True'
									else: return 'True'
								elif obj[9]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[6]>4:
								return 'True'
							else: return 'True'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[7]>21:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[6]>0:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]<=16:
							return 'False'
						elif obj[7]>16:
							return 'True'
						else: return 'True'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[8]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 34, "metric_value": 0.9082, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.684, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[7]>4:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2:
							return 'False'
						elif obj[4]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]<=4:
					# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[8]<=0.0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>1:
							return 'False'
						elif obj[4]<=1:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]>1.0:
				return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[7]<=15:
				# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[4]>4:
					# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>2:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							elif obj[1]<=2:
								return 'True'
							else: return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[8]>2.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=4:
					return 'True'
				else: return 'True'
			elif obj[7]>15:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
