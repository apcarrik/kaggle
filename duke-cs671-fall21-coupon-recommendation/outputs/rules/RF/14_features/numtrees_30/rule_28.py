def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[12]<=0:
		# {"feature": "Age", "instances": 25, "metric_value": 0.9896, "depth": 2}
		if obj[4]<=4:
			# {"feature": "Distance", "instances": 21, "metric_value": 0.9183, "depth": 3}
			if obj[13]>1:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[7]<=9:
					return 'True'
				elif obj[7]>9:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[13]<=1:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>4:
			return 'False'
		else: return 'False'
	elif obj[12]>0:
		return 'True'
	else: return 'True'
