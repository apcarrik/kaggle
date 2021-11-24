def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[12]<=17:
		# {"feature": "Income", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[13]>0:
			# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[15]<=2.0:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[19]>1:
					# {"feature": "Driving_to", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[9]>0:
							# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[6]>0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[9]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[19]<=1:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=4:
						return 'True'
					elif obj[8]>4:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[15]>2.0:
				return 'False'
			else: return 'False'
		elif obj[13]<=0:
			return 'True'
		else: return 'True'
	elif obj[12]>17:
		return 'True'
	else: return 'True'
