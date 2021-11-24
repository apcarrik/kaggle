def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Income", "instances": 20, "metric_value": 0.9928, "depth": 1}
	if obj[13]<=6:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[15]<=2.0:
			# {"feature": "Temperature", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[3]<=55:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[12]>3:
					# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=3:
					return 'False'
				else: return 'False'
			elif obj[3]>55:
				return 'False'
			else: return 'False'
		elif obj[15]>2.0:
			return 'True'
		else: return 'True'
	elif obj[13]>6:
		return 'True'
	else: return 'True'
