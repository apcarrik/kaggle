def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[12]<=1.0:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Direction_same", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[15]<=0:
				# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[2]<=1:
					return 'False'
				elif obj[2]>1:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[15]>0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	elif obj[12]>1.0:
		return 'True'
	else: return 'True'
