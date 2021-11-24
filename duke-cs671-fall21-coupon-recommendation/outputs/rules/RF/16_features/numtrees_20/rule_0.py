def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[10]<=6:
		# {"feature": "Age", "instances": 46, "metric_value": 0.9986, "depth": 2}
		if obj[6]<=4:
			# {"feature": "Distance", "instances": 42, "metric_value": 0.9984, "depth": 3}
			if obj[15]<=2:
				# {"feature": "Coupon", "instances": 38, "metric_value": 0.998, "depth": 4}
				if obj[3]>1:
					# {"feature": "Time", "instances": 27, "metric_value": 0.951, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[9]<=12:
							# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[11]<=2.0:
								# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[8]<=3:
									# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[4]>0:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[0]>0:
											return 'False'
										elif obj[0]<=0:
											# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1]<=0:
												return 'True'
											elif obj[1]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[0]>2:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[12]>0.0:
												return 'True'
											elif obj[12]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[0]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>3:
									return 'True'
								else: return 'True'
							elif obj[11]>2.0:
								return 'False'
							else: return 'False'
						elif obj[9]>12:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[9]<=7:
						return 'False'
					elif obj[9]>7:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[11]<=2.0:
							return 'True'
						elif obj[11]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[15]>2:
				return 'False'
			else: return 'False'
		elif obj[6]>4:
			return 'True'
		else: return 'True'
	elif obj[10]>6:
		return 'True'
	else: return 'True'
