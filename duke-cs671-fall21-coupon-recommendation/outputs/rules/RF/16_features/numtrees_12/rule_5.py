def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Age", "instances": 68, "metric_value": 0.9944, "depth": 2}
		if obj[6]<=5:
			# {"feature": "Passanger", "instances": 60, "metric_value": 1.0, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 45, "metric_value": 0.9825, "depth": 4}
				if obj[9]<=17:
					# {"feature": "Bar", "instances": 42, "metric_value": 0.9587, "depth": 5}
					if obj[11]<=3.0:
						# {"feature": "Time", "instances": 40, "metric_value": 0.9341, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Coupon_validity", "instances": 32, "metric_value": 0.8571, "depth": 7}
							if obj[4]<=0:
								# {"feature": "Coupon", "instances": 17, "metric_value": 0.9774, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Children", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											return 'False'
										elif obj[1]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>2:
									# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[12]<=1.0:
											# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[10]>2:
												return 'True'
											elif obj[10]<=2:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[14]<=0:
													return 'False'
												elif obj[14]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[12]>1.0:
											return 'False'
										else: return 'False'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>0:
								# {"feature": "Income", "instances": 15, "metric_value": 0.5665, "depth": 8}
								if obj[10]<=5:
									return 'False'
								elif obj[10]>5:
									# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[3]>2:
										return 'False'
									elif obj[3]<=2:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[2]>3:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[13]<=1.0:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[12]<=1.0:
									return 'False'
								elif obj[12]>1.0:
									return 'True'
								else: return 'True'
							elif obj[13]>1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[11]>3.0:
						return 'True'
					else: return 'True'
				elif obj[9]>17:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[9]<=10:
					# {"feature": "Income", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[10]>0:
						return 'True'
					elif obj[10]<=0:
						# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]>10:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>5:
			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]<=1:
				return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>2:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[9]<=20:
			# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[4]<=0:
				return 'True'
			elif obj[4]>0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[12]>1.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[12]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[9]>20:
			return 'False'
		else: return 'False'
	else: return 'True'
