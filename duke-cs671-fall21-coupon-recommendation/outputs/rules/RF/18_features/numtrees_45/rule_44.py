def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.6666, "depth": 1}
	if obj[11]>2:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[10]>3:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		elif obj[10]<=3:
			return 'True'
		else: return 'True'
	elif obj[11]<=2:
		return 'True'
	else: return 'True'
