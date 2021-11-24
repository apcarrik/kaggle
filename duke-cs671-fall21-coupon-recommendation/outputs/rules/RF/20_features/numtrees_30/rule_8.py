def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[17]<=1.0:
		# {"feature": "Coupon", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[5]>0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[12]<=15:
				# {"feature": "Restaurantlessthan20", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[16]>1.0:
					# {"feature": "Weather", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[7]>0:
							# {"feature": "Driving_to", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]<=0:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[11]>0:
									return 'True'
								elif obj[11]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>0:
								return 'False'
							else: return 'False'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				elif obj[16]<=1.0:
					return 'True'
				else: return 'True'
			elif obj[12]>15:
				return 'False'
			else: return 'False'
		elif obj[5]<=0:
			return 'False'
		else: return 'False'
	elif obj[17]>1.0:
		# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[13]>2:
			return 'True'
		elif obj[13]<=2:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
