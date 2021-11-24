def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>0:
		# {"feature": "Age", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[6]>0:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[12]<=0.0:
				return 'True'
			elif obj[12]>0.0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]<=0:
			return 'False'
		else: return 'False'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'
