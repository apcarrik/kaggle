def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[9]<=2:
			# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[14]<=2.0:
				return 'True'
			elif obj[14]>2.0:
				return 'False'
			else: return 'False'
		elif obj[9]>2:
			# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
