def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[9]>4:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[3]>1:
			# {"feature": "Gender", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[5]>0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[8]<=2:
					return 'True'
				elif obj[8]>2:
					return 'False'
				else: return 'False'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			return 'False'
		else: return 'False'
	elif obj[9]<=4:
		return 'True'
	else: return 'True'
