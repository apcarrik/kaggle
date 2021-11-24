def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[14]<=3.0:
		# {"feature": "Age", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Temperature", "instances": 20, "metric_value": 1.0, "depth": 3}
			if obj[2]>55:
				# {"feature": "Income", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[12]>2:
					# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[10]<=3:
						return 'True'
					elif obj[10]>3:
						return 'False'
					else: return 'False'
				elif obj[12]<=2:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[11]>0:
						return 'False'
					elif obj[11]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=55:
				# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[15]<=3.0:
					return 'False'
				elif obj[15]>3.0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[7]>2:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[11]<=14:
				return 'True'
			elif obj[11]>14:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[14]>3.0:
		return 'False'
	else: return 'False'
