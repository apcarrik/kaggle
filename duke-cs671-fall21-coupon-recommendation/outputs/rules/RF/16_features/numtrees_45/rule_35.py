def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon_validity", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[3]<=3:
				return 'True'
			elif obj[3]>3:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[9]>1:
					return 'False'
				elif obj[9]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[4]>0:
		return 'True'
	else: return 'True'
