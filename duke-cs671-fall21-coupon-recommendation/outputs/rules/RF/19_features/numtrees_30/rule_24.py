def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon_validity", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[5]>0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[4]>3:
			# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[7]>0:
				return 'False'
			elif obj[7]<=0:
				return 'True'
			else: return 'True'
		elif obj[4]<=3:
			# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[15]>1.0:
				return 'True'
			elif obj[15]<=1.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Income", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[12]<=6:
			return 'True'
		elif obj[12]>6:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]>2:
				return 'True'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
