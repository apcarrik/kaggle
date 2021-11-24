def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]>4:
		# {"feature": "Distance", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[13]<=2:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[9]>0.0:
					return 'True'
				elif obj[9]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[13]>2:
			return 'False'
		else: return 'False'
	elif obj[7]<=4:
		# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[13]<=2:
			return 'False'
		elif obj[13]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
