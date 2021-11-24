def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Income", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[9]<=4:
			# {"feature": "Direction_same", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[13]<=0:
				return 'False'
			elif obj[13]>0:
				# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>4:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[7]<=0:
				return 'True'
			elif obj[7]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
