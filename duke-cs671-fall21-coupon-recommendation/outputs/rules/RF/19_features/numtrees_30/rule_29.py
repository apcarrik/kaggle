def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[15]<=3.0:
		# {"feature": "Passanger", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[0]>0:
			# {"feature": "Coupon", "instances": 25, "metric_value": 0.795, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.5917, "depth": 4}
				if obj[16]>0.0:
					# {"feature": "Income", "instances": 18, "metric_value": 0.3095, "depth": 5}
					if obj[12]<=7:
						return 'True'
					elif obj[12]>7:
						return 'False'
					else: return 'False'
				elif obj[16]<=0.0:
					# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=55:
					return 'False'
				elif obj[2]>55:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[15]>3.0:
		return 'False'
	else: return 'False'
