def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[11]>1:
		# {"feature": "Distance", "instances": 42, "metric_value": 0.9737, "depth": 2}
		if obj[18]<=2:
			# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.9268, "depth": 3}
			if obj[16]<=1.0:
				# {"feature": "Income", "instances": 26, "metric_value": 0.9957, "depth": 4}
				if obj[12]<=4:
					# {"feature": "Education", "instances": 18, "metric_value": 0.8524, "depth": 5}
					if obj[10]<=2:
						# {"feature": "Temperature", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[2]>30:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[17]<=0:
								# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=3:
									# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[3]>0:
										# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[4]>1:
											# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0]>2:
												return 'True'
											elif obj[0]<=2:
												return 'False'
											else: return 'False'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[7]>3:
									return 'True'
								else: return 'True'
							elif obj[17]>0:
								return 'False'
							else: return 'False'
						elif obj[2]<=30:
							return 'True'
						else: return 'True'
					elif obj[10]>2:
						return 'True'
					else: return 'True'
				elif obj[12]>4:
					# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[7]<=5:
						return 'False'
					elif obj[7]>5:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1:
							return 'True'
						elif obj[4]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[16]>1.0:
				# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[18]>2:
			return 'False'
		else: return 'False'
	elif obj[11]<=1:
		return 'True'
	else: return 'True'
