def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[13]<=2:
		# {"feature": "Age", "instances": 76, "metric_value": 0.9955, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Restaurant20to50", "instances": 70, "metric_value": 1.0, "depth": 3}
			if obj[11]<=1.0:
				# {"feature": "Children", "instances": 41, "metric_value": 0.9474, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Gender", "instances": 28, "metric_value": 0.9963, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 6}
						if obj[2]>1:
							# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[7]<=7:
									# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[8]<=4:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1]<=3:
												return 'False'
											elif obj[1]>3:
												return 'True'
											else: return 'True'
										elif obj[8]>4:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[7]>7:
									return 'False'
								else: return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]>0:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[10]<=2.0:
							return 'True'
						elif obj[10]>2.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]<=0:
										return 'True'
									elif obj[6]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[5]>0:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[7]<=17:
						return 'False'
					elif obj[7]>17:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[11]>1.0:
				# {"feature": "Passanger", "instances": 29, "metric_value": 0.8936, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Income", "instances": 23, "metric_value": 0.9656, "depth": 5}
					if obj[8]<=6:
						# {"feature": "Occupation", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=6:
							# {"feature": "Bar", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[6]>0:
									# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[1]<=1:
										return 'False'
									elif obj[1]>1:
										# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=0:
												return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=0:
									# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[10]<=3.0:
										return 'True'
									elif obj[10]>3.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[9]>2.0:
								return 'True'
							else: return 'True'
						elif obj[7]>6:
							return 'True'
						else: return 'True'
					elif obj[8]>6:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>6:
			return 'True'
		else: return 'True'
	elif obj[13]>2:
		# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[4]>0:
			return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
