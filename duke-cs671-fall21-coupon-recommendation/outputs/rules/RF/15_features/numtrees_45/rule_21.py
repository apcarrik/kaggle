def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[8]>1:
		# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[11]>0.0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[8]<=1:
		return 'True'
	else: return 'True'
