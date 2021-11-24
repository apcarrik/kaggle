def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[5]>0:
		# {"feature": "Age", "instances": 31, "metric_value": 0.8238, "depth": 2}
		if obj[8]<=6:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.7355, "depth": 3}
			if obj[12]<=6:
				# {"feature": "Driving_to", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Income", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[13]<=4:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[1]>1:
							# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[11]<=0:
									return 'False'
								elif obj[11]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					elif obj[13]>4:
						# {"feature": "Temperature", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[3]<=55:
							return 'True'
						elif obj[3]>55:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>1:
								return 'True'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[12]>6:
				return 'True'
			else: return 'True'
		elif obj[8]>6:
			return 'False'
		else: return 'False'
	elif obj[5]<=0:
		return 'False'
	else: return 'False'
