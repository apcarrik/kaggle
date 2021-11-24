def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Education", "instances": 41, "metric_value": 0.9892, "depth": 1}
	if obj[11]>1:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9612, "depth": 2}
		if obj[12]>3:
			# {"feature": "Income", "instances": 20, "metric_value": 1.0, "depth": 3}
			if obj[13]>1:
				# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[9]<=1:
					# {"feature": "Carryaway", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[16]>1.0:
						# {"feature": "Children", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[10]<=0:
							return 'True'
						elif obj[10]>0:
							# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[16]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[9]>1:
					return 'False'
				else: return 'False'
			elif obj[13]<=1:
				return 'False'
			else: return 'False'
		elif obj[12]<=3:
			return 'False'
		else: return 'False'
	elif obj[11]<=1:
		# {"feature": "Income", "instances": 15, "metric_value": 0.5665, "depth": 2}
		if obj[13]>2:
			return 'True'
		elif obj[13]<=2:
			# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[15]<=0.0:
				return 'False'
			elif obj[15]>0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
