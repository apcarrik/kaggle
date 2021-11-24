def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[6]>0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[7]<=8:
					return 'False'
				elif obj[7]>8:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[10]>1.0:
						return 'True'
					elif obj[10]<=1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[9]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
