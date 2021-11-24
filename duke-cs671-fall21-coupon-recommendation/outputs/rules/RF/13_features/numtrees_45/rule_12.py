def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[8]<=2.0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[2]>3:
			return 'False'
		elif obj[2]<=3:
			# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[11]<=0:
					return 'False'
				elif obj[11]>0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]>2.0:
		return 'True'
	else: return 'True'
