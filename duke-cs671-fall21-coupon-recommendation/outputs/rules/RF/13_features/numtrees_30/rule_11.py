def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[7]<=9:
		# {"feature": "Distance", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[12]>1:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[10]<=2.0:
					# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[9]>2.0:
						return 'False'
					else: return 'False'
				elif obj[10]>2.0:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[12]<=1:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[7]>9:
		return 'False'
	else: return 'False'
