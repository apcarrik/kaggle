def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]>1:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[11]<=12:
			# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]>12:
			return 'False'
		else: return 'False'
	elif obj[4]<=1:
		# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[7]<=6:
			return 'False'
		elif obj[7]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
