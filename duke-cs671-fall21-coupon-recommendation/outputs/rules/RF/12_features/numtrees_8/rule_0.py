def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 84, "metric_value": 0.9587, "depth": 2}
		if obj[0]>0:
			# {"feature": "Bar", "instances": 79, "metric_value": 0.9738, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Education", "instances": 69, "metric_value": 0.9446, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.8709, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Age", "instances": 32, "metric_value": 0.9544, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[6]>5:
								# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 8}
								if obj[1]>1:
									# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=1:
									return 'False'
								else: return 'False'
							elif obj[6]<=5:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]>1.0:
									return 'True'
								elif obj[8]<=1.0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										return 'False'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[4]>2:
							# {"feature": "Direction_same", "instances": 15, "metric_value": 0.7219, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[6]<=7:
									# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[1]>0:
										# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[8]>1.0:
											# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[11]>1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										elif obj[8]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]>0.0:
											return 'True'
										elif obj[8]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]>7:
									return 'False'
								else: return 'False'
							elif obj[10]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[9]>1.0:
						# {"feature": "Occupation", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[6]>0:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3712, "depth": 7}
							if obj[10]<=0:
								return 'True'
							elif obj[10]>0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]<=0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>2:
								return 'True'
							elif obj[1]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[5]>2:
					# {"feature": "Age", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[4]<=5:
						# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											return 'True'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]>0:
									return 'False'
								else: return 'False'
							elif obj[9]>1.0:
								return 'True'
							else: return 'True'
						elif obj[8]>1.0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[3]>0:
									# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]<=6:
											return 'True'
										elif obj[6]>6:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[10]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>5:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[7]>2.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[6]<=10:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]>0.0:
							return 'True'
						elif obj[8]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]>10:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 43, "metric_value": 0.9103, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.6769, "depth": 3}
			if obj[6]>5:
				# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]>2:
								return 'False'
							elif obj[5]<=2:
								return 'True'
							else: return 'True'
						elif obj[3]>0:
							return 'False'
						else: return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[6]<=5:
				return 'False'
			else: return 'False'
		elif obj[7]>1.0:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[10]<=0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[6]<=9:
							# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]>2:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]>2.0:
									return 'True'
								elif obj[8]<=2.0:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						elif obj[6]>9:
							return 'True'
						else: return 'True'
					elif obj[10]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
