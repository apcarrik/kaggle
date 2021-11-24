def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Children", "instances": 85, "metric_value": 0.9259, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Passanger", "instances": 56, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coffeehouse", "instances": 37, "metric_value": 0.909, "depth": 3}
			if obj[9]>1.0:
				# {"feature": "Education", "instances": 24, "metric_value": 0.995, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 1.0, "depth": 5}
					if obj[10]<=2.0:
						# {"feature": "Time", "instances": 21, "metric_value": 0.9984, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Distance", "instances": 20, "metric_value": 1.0, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 8}
								if obj[2]>1:
									# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[7]<=6:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[3]>0:
												# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[4]>2:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[4]<=2:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[7]>6:
										return 'False'
									else: return 'False'
								elif obj[2]<=1:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]>1:
										return 'True'
									elif obj[7]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[12]>2:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[10]>2.0:
						return 'True'
					else: return 'True'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			elif obj[9]<=1.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[7]<=9:
					return 'True'
				elif obj[7]>9:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Age", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[4]>3:
				return 'True'
			elif obj[4]<=3:
				# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[6]<=2:
						return 'True'
					elif obj[6]>2:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=16:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=1:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>16:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[5]>0:
		# {"feature": "Age", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[4]>0:
			# {"feature": "Education", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[6]<=1:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[2]>0:
					# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[7]<=12:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[7]>12:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[6]>1:
				# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[1]>0:
					# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[7]>2:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[9]<=3.0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]<=1.0:
									return 'True'
								elif obj[8]>1.0:
									return 'False'
								else: return 'False'
							elif obj[9]>3.0:
								return 'False'
							else: return 'False'
						elif obj[7]<=2:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
