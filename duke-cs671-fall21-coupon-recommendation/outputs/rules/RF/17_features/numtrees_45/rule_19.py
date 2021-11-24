def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[10]>5:
		# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[7]>0:
			# {"feature": "Children", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[8]<=0:
				return 'True'
			elif obj[8]>0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>2:
					return 'True'
				elif obj[0]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=0:
			# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=4:
				return 'False'
			elif obj[6]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]<=5:
		return 'True'
	else: return 'True'
