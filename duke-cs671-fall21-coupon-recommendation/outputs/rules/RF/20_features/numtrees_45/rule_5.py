def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Driving_to", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[12]>5:
			return 'False'
		elif obj[12]<=5:
			# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[9]<=0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[12]<=14:
			return 'True'
		elif obj[12]>14:
			return 'False'
		else: return 'False'
	else: return 'True'
