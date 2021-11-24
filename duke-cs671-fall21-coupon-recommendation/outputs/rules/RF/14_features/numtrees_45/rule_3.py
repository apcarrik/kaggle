def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[12]<=0:
			# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[6]<=2:
				return 'False'
			elif obj[6]>2:
				# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]>0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
