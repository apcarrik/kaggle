def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[17]<=1.0:
		# {"feature": "Income", "instances": 37, "metric_value": 0.9868, "depth": 2}
		if obj[13]<=5:
			# {"feature": "Direction_same", "instances": 25, "metric_value": 0.8555, "depth": 3}
			if obj[18]<=0:
				# {"feature": "Age", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[8]>0:
					# {"feature": "Gender", "instances": 18, "metric_value": 0.5033, "depth": 5}
					if obj[7]>0:
						return 'False'
					elif obj[7]<=0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[12]>2:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[15]<=1.0:
								return 'False'
							elif obj[15]>1.0:
								# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]<=0:
					# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]<=0:
						return 'True'
					elif obj[0]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[18]>0:
				return 'True'
			else: return 'True'
		elif obj[13]>5:
			# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[9]>0:
				return 'True'
			elif obj[9]<=0:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=2:
					return 'False'
				elif obj[8]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[17]>1.0:
		# {"feature": "Income", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[13]>1:
			return 'True'
		elif obj[13]<=1:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
