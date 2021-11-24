def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[4]>0:
		# {"feature": "Temperature", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[3]>30:
			# {"feature": "Age", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[8]>0:
				# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[15]>0.0:
					# {"feature": "Coupon", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[14]<=1.0:
							# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[11]>0:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[19]<=1:
									# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]<=0:
											return 'False'
										elif obj[7]>0:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								elif obj[19]>1:
									return 'False'
								else: return 'False'
							elif obj[11]<=0:
								return 'True'
							else: return 'True'
						elif obj[14]>1.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[15]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[8]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]<=30:
			return 'True'
		else: return 'True'
	elif obj[4]<=0:
		return 'True'
	else: return 'True'
