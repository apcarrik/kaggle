def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[6]<=21:
		# {"feature": "Bar", "instances": 80, "metric_value": 0.9778, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Education", "instances": 68, "metric_value": 0.9488, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.9896, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Time", "instances": 26, "metric_value": 0.8905, "depth": 5}
					if obj[1]>0:
						# {"feature": "Age", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[4]<=3:
							return 'False'
						elif obj[4]>3:
							# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[2]>1:
								# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[0]>0:
									# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[11]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>2.0:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=4:
								return 'False'
							elif obj[4]>4:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[9]>1.0:
					# {"feature": "Time", "instances": 24, "metric_value": 0.9799, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Gender", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[3]>0:
							# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[11]<=1:
								# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[2]>1:
									# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]>1.0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4]>2:
												return 'False'
											elif obj[4]<=2:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[8]<=1.0:
										return 'True'
									else: return 'True'
								elif obj[2]<=1:
									return 'False'
								else: return 'False'
							elif obj[11]>1:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=2:
								return 'False'
							elif obj[2]>2:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[8]>1.0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[11]<=2:
											return 'False'
										elif obj[11]>2:
											return 'True'
										else: return 'True'
									elif obj[4]>4:
										return 'False'
									else: return 'False'
								elif obj[8]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]>2:
				# {"feature": "Time", "instances": 18, "metric_value": 0.65, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.3534, "depth": 5}
					if obj[8]<=3.0:
						return 'False'
					elif obj[8]>3.0:
						# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=0:
							return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]<=1:
						return 'True'
					elif obj[11]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[7]>2.0:
			# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=1:
				return 'True'
			elif obj[4]>1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[6]>21:
		return 'True'
	else: return 'True'
