def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[8]<=7:
		# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	elif obj[8]>7:
		# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[13]<=0:
			return 'False'
		elif obj[13]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
