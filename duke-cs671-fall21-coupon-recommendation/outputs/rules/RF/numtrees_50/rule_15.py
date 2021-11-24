def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Income", "instances": 20, "metric_value": 0.9928, "depth": 1}
	if obj[13]>1:
		# {"feature": "Weather", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[2]<=0:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[15]<=2.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[12]>1:
					# {"feature": "Carryaway", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[16]>1.0:
						return 'False'
					elif obj[16]<=1.0:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[20]>1:
							return 'True'
						elif obj[20]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			elif obj[15]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]>0:
			return 'True'
		else: return 'True'
	elif obj[13]<=1:
		return 'False'
	else: return 'False'
