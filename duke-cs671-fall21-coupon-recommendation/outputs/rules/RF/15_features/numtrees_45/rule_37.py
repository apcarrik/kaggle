def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[12]>0.0:
		# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[7]>0:
			# {"feature": "Children", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[6]>0:
				return 'False'
			elif obj[6]<=0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=0:
			return 'True'
		else: return 'True'
	elif obj[12]<=0.0:
		return 'True'
	else: return 'True'
