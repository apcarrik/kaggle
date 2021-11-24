def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[10]<=17:
		# {"feature": "Distance", "instances": 47, "metric_value": 0.9441, "depth": 2}
		if obj[17]<=2:
			# {"feature": "Weather", "instances": 43, "metric_value": 0.9103, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.9569, "depth": 4}
				if obj[15]>0.0:
					# {"feature": "Bar", "instances": 33, "metric_value": 0.9834, "depth": 5}
					if obj[12]<=0.0:
						# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[13]>0.0:
							# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[5]>0:
									return 'False'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[13]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[12]>0.0:
						# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[9]<=3:
									return 'True'
								elif obj[9]>3:
									return 'False'
								else: return 'False'
							elif obj[3]>2:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[15]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[17]>2:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[9]<=1:
				return 'False'
			elif obj[9]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]>17:
		return 'True'
	else: return 'True'
